import React from "react";
import { useNavigate } from "react-router-dom"; // Thêm dòng này
import "./RestaurantCard.css";

function RestaurantCard({ 
  id,  // hoặc IdRestaurant (tùy bạn đặt tên gì)
  name, 
  address, 
  district, 
  average_rating, 
  delivery_url, 
  image 
}) {
  const navigate = useNavigate();

  const handleNameClick = () => {
    navigate(`/restaurant/${id}`);
  };

  return (
    <div className="restaurant-card">
      <div className="restaurant-image-wrapper">
        <img
          src={
            image ||
            "https://static.vecteezy.com/system/resources/previews/013/698/221/original/restaurant-building-color-icon-clip-art-illustration-free-vector.jpg"
          }
          alt={name}
          className="restaurant-image"
        />
        <a
          href={delivery_url}
          className="restaurant-delivery-link"
          target="_blank"
          rel="noopener noreferrer"
        >
          Xem trên ShopeeFood
        </a>
      </div>
      <div className="restaurant-info">
        <span className="restaurant-dish" style={{ cursor: 'pointer' }} onClick={handleNameClick}>
          <h3 className="restaurant-name">{name}</h3>
        </span>
        <div className="restaurant-rating">
          <span>⭐</span> {average_rating}
        </div>
        {district && (
          <div className="restaurant-district">
            <b>Quận:</b> {district}
          </div>
        )}
        <div className="restaurant-address">{address}</div>
      </div>
    </div>
  );
}

export default RestaurantCard;
