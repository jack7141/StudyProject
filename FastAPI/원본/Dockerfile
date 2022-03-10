# # ------------------------------------------------------------------------------
# # Base image
# # ------------------------------------------------------------------------------
# FROM python:3.10
# # ------------------------------------------------------------------------------
# # Install Server with python
# # ------------------------------------------------------------------------------
# RUN apt-get update 
# RUN apt-get install -y nginx 

# COPY requirements.txt /tmp/requirements.txt
# RUN python3 -m pip install -r /tmp/requirements.txt
# # RUN pip3 install -r requirements.txt
# # ------------------------------------------------------------------------------
# # PORT EXPOSE
# # ------------------------------------------------------------------------------
# EXPOSE 8000
# # ------------------------------------------------------------------------------
# # Install dependencies
# # ------------------------------------------------------------------------------
# # CMD ["nginx", "-g", "daemon off;"]
# WORKDIR /app
# CMD ["uvicorn", "app.main:create_app()", "--host=0.0.0.0", "--reload"]
FROM python:3.10
 
COPY ./app /app
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
# RUN pip install -r requirements.txt
 
EXPOSE 80
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]