import thread

def app(environ, start_response): # pragma: no cover
    thread.interrupt_main()
