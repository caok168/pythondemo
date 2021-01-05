import sys, os, subprocess, time, signal
p = subprocess.Popen(['google-chrome',"http://www.baidu.com"], close_fds=True, preexec_fn = os.setsid)
print(p.pid)
time.sleep(5)
# p.kill() #无法杀掉所有子进程，只能杀掉子shell的进程

# p.terminate()  #无法杀掉所有子进程
os.killpg(p.pid, signal.SIGUSR1)

time.sleep(3)
