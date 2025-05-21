import React from "react";
import "./RestaurantDetailCard.css";

function RestaurantDetailCard({
  name, 
  address, 
  district, 
  average_rating,
  delivery_url, 
}) {
  return (
    <div className="detailcard-root">
      <div className="detailcard-logo-wrap">
        <img className="detailcard-logo" src="https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45" alt="logo" />
      </div>
      <div className="detailcard-info-wrap">
        <div className="detailcard-title">{name}</div>
        <div className="detailcard-scores">
          <span className="score-first">
            <span className="score-circle">{average_rating}</span>
            <h3>Điểm đánh giá</h3>
          </span>
        </div>
        <div className="detailcard-address">
          <span className="detailcard-icon">📍</span>
          {address}, <span style={{fontWeight:500}}>Quận {district}, Đà Nẵng</span>
        </div>
        <div>
          <a className="link-to-shopee" href="/">Xem trên ShopeeFood</a>
        </div>
      </div>
    </div>
  );
}

export default RestaurantDetailCard;
