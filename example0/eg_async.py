
async def get_data():
    return {"data": "Foo"}

async def logic():
    data = await get_data()
    return response

@app.get("/")
async def root():
    return await logic()