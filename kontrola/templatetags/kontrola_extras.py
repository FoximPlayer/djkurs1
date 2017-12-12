import os, sys
import datetime
import psutil
from django import template
from psutil import virtual_memory
from psutil import cpu_times, cpu_count
from psutil import process_iter
from django.utils.safestring import mark_safe

register = template.Library()

procs = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'pid', 'username',])}
processes = procs



@register.simple_tag
def ctime(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def cpu():
    cpu1 = cpu_times()

    return mark_safe('''
	    <ul>
            <li>user: {user}</li>
            <li>nice: {nice}</li>
            <li>system: {system}</li>
            <li>idle: {idle}</li>
            <li>iowait: {iowait}</li>
            <li>irq: {irq}</li>
            <li>softirq: {softirq}</li>
            <li>steal: {steal}</li>
            <li>guest: {guest}</li>
            <li>number_of_cpu: {number_of_cpu}</li>
            <li>load_avg: {load_avg}</li>
	    </ul>
	    '''.format(
	        user = cpu1.user,
	        system = cpu1.system,
	        idle = cpu1.idle,
	        iowait = cpu1.iowait,
	        irq = cpu1.irq,
	        softirq = cpu1.softirq,
	        steal = cpu1.steal,
	        guest = cpu1.guest,
	        nice = cpu1.nice,
	        number_of_cpu = cpu_count(),
	        load_avg = os.getloadavg()
	    ))


@register.simple_tag
def mem():
    memvirt = virtual_memory()

    return mark_safe('''
        <ul>
            <li>free: {free}</li>
            <li>total: {total}</li>
            <li>cached: {cached}</li>
            <li>active: {active}</li>
            <li>percent: {percent}</li>
            <li>available: {available}</li>
            <li>used: {used}</li>
            <li>inactive: {inactive}</li>
            <li>buffers: {buffers}</li>
            <li>shared: {shared}</li>
        </ul>
    	'''.format(
            free = memvirt.free,
            total = memvirt.total,
            cached = memvirt.cached,
            active = memvirt.active,
            percent = memvirt.percent,
            available = memvirt.available,
            used = memvirt.used,
            inactive = memvirt.inactive,
            buffers = memvirt.buffers,
            shared = memvirt.shared,
            ))

@register.simple_tag
def process():
	proc = psutil.process_iter(attrs=None, ad_value=None)

	return mark_safe('''
		<ul>
			<li>Processes: {processes}</li>
		</ul>
		'''.format(
			processes = processes
			))

