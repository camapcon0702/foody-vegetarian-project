import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-top">
        <div className="footer-col">
          <h4>Khám phá</h4>
          <a href="#">Ứng dụng Mobile</a>
          <a href="#">Tạo bộ sưu tập</a>
          <a href="#">Bảo mật thông tin</a>
          <a href="#">Quy định</a>
        </div>
        <div className="footer-col">
          <h4>Công ty</h4>
          <a href="#">Giới thiệu</a>
          <a href="#">Trợ giúp</a>
          <a href="#">Việc làm</a>
          <a href="#">Quy chế</a>
          <a href="#">Thỏa thuận sử dụng dịch vụ</a>
          <a href="#">Liên hệ</a>
        </div>
        <div className="footer-col">
          <h4>Tham gia trên</h4>
          <a href="#">Facebook</a>
          <a href="#">Instagram</a>
          <a href="#">Youtube</a>
          <a href="#">Google</a>
          <a href="#">ShopeeFood.vn <span className="footer-note">- Giao đồ ăn tận nơi</span></a>
        </div>
        <div className="footer-col">
          <h4>Giấy phép</h4>
          <a href="#" className="footer-license">MXH 363/GP-BTTTT</a>
          <img
            src="https://cdn.dangkywebsitevoibocongthuong.com/wp-content/uploads/2018/06/logo.png"
            alt="Đã đăng ký Bộ Công Thương"
            className="footer-bct"
          />
        </div>
      </div>
      <div className="footer-bottom">
        <div className="footer-company">
          Công Ty Cổ Phần Foody, Lầu G, Tòa nhà Jabes 1, 244 đường Cống Quỳnh, phường Phạm Ngũ Lão, Quận 1, TP.HCM<br />
          Email: <a href="mailto:support@shopeefood.vn">support@shopeefood.vn</a>
        </div>
        <div className="footer-license-info">
          Giấy CN ĐKDN số 0311828036 do Sở Kế hoạch và Đầu tư TP.HCM cấp ngày 11/6/2012, sửa đổi lần thứ 23, ngày 10/12/2020<br />
          Giấy phép thiết lập MXH trên mạng số 363/GP-BTTTT do Bộ Thông tin và Truyền thông cấp ngày 30/6/2016
          Người chịu trách nhiệm: Đặng Hoàng Minh.
        </div>
      </div>
    </footer>
  );
}

export default Footer;
