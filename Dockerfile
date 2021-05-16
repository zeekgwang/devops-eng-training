# Docker Base Image
FROM python:3.9

# 현재 경로에 있는 파일을 도커 이미지로 복사
COPY . /app

# 도커 이미지의 현재 디렉토리 변경
WORKDIR /app

# 쉘 스크립트 실행
RUN pip install -r requirements.txt

# 컨테이너가 실행 되었을 때 실행되는 명령어
CMD ["python", "app.py"]