from pydantic import BaseModel, Field


class SpeedTestResult(BaseModel):
    download: float = Field(description="Download speed in bits per second")
    upload: float = Field(description="Upload speed in bits per second")
    ping: float = Field(description="Ping in milliseconds")

