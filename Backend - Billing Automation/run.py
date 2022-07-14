import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="192.168.43.178", port=8080, reload=True)