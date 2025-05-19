import React from "react";
import './ListRestaurant.css';
import RestaurantCard from "../RestaurantCard/RestaurantCard";

function ListRestaurant({ nameTitle,  restaurants }) {
  if (!restaurants || restaurants.length === 0) {
    return <div className="listrestaurant-empty">Không có nhà hàng nào để hiển thị.</div>;
  }

  return (
    <>
        <div className="title-list">{nameTitle}</div>
    
                 <div className="listrestaurant-wrapper">
                    {restaurants.map((item) => (
                        <RestaurantCard
                        key={item.IdRestaurant}
                        name={item.name}
                        address={item.address}
                        district={item.district}
                        average_rating={item.average_rating}
                        delivery_url={item.delivery_url}
                        image={item.image}
                        />
                    ))}
                </div>
               
    </>
    
  );
}

export default ListRestaurant;
