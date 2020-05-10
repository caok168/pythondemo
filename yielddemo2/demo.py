
def gen_func():
    # 1. 可以产出值， 2. 可以接收值（调用方传递进来的值）
    html = yield "http://projectedu.com"
    print(html)
    yield 2
    yield 3
    return "ck"

# 1. 生成器不只可以产出值，还可以接收值

if __name__ == "__main__":
    gen = gen_func()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种 1. gen.send(None), 2. next(gen)
    url = next(gen)
    print(url)
    html = "ck"
    # send 方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield
    print(gen.send(html))
