from aiohttp import web

async def handle_request(request):
    url = request.url.with_scheme("https").with_host("archnet.coloringco.com.au")
    new_request = request.clone(rel_url=url)
    async with aiohttp.ClientSession() as session:
        async with session.request(method=new_request.method, url=new_request.url, headers=new_request.headers) as response:
            headers = {key.lower(): value for key, value in response.headers.items()}
            body = await response.read()
            return web.Response(body=body, status=response.status, headers=headers)

if __name__ == '__main__':
    app = web.Application()
    app.router.add_route('*', '/{tail:.*}', handle_request)
    web.run_app(app)