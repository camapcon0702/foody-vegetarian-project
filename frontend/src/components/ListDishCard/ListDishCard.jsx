import React from "react";
import DishCard from "../DishCard/DishCard";
import "./ListDishCard.css";

function ListDishCard({ dishes }) {
  if (!dishes || dishes.length === 0) {
    return <div className="listdishcard-empty">Không có món ăn nào để hiển thị.</div>;
  }

  return (
    <>
      <div className="title-list-dish">
        <h3>Danh sách món ăn</h3>
      </div>
      <div className="listdishcard-root">
        {dishes.map((dish, idx) => (
          <DishCard
            key={dish.id || idx}
            image={dish.image}
            name={dish.name}
            price={dish.price}
          />
        ))}
      </div>
    </>
  );
}

export default ListDishCard;
