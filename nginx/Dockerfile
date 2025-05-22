# FROM nginx:latest
# COPY conf/nginx.conf /etc/nginx/nginx.conf


# Copy dist build từ frontend builder - giai đoạn này ta sẽ mount volume hoặc copy thủ công trong docker-compose

# Ví dụ nếu dùng volume:
# Chúng ta sẽ mount thư mục dist từ host vào /usr/share/nginx/html trong container nginx

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]

FROM nginx:alpine
COPY conf/nginx.conf /etc/nginx/nginx.conf
