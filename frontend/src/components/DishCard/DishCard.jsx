import React from "react";
import "./DishCard.css";

function DishCard({ image, name, price }) {
  return (
    <div className="dishcard-root">
      <img src={image} alt={name} className="dishcard-img" />
      <div className="dishcard-name">{name}</div>
      <div className="dishcard-price">{price}</div>
    </div>
  );
}

export default DishCard;