
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 创建 FastAPI 应用
app = FastAPI(
    title="Job Intelligence Platform API",
    description="职位数据展示与分析中台接口",
    version="0.1.0"
)

# 配置前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 首页接口
@app.get("/")
def read_root():
    return {
        "message": "Job Intelligence Platform API is running"
    }


# 健康检查接口
@app.get("/api/v1/health")
def health_check():
    return {
        "status": "ok",
        "service": "job-intelligence-platform-api"
    }
