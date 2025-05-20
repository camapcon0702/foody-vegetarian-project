import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../components/Header/Header';
import RestaurantDetailCard from '../components/DetailsRestaurant/RestaurantDetailCard';
import ListDishCard from '../components/ListDishCard/ListDishCard';
import Footer from '../components/Footer/Footer';

export default function DetailsRestaurantPage() {
  const { id } = useParams();

  // State cho nhà hàng
  const [restaurant, setRestaurant] = useState(null);
  const [loadingRestaurant, setLoadingRestaurant] = useState(true);

  // State cho món ăn
  const [dishes, setDishes] = useState([]);
  const [loadingDishes, setLoadingDishes] = useState(true);

  // Gọi API lấy info nhà hàng
  useEffect(() => {
    setLoadingRestaurant(true);
    fetch(`http://localhost:8080/api/v1/restaurants/${id}`)
      .then(res => res.json())
      .then(data => {
        setRestaurant(data);
        setLoadingRestaurant(false);
      })
      .catch(() => {
        setRestaurant(null);
        setLoadingRestaurant(false);
      });
  }, [id]);

  // Gọi API lấy món ăn
  useEffect(() => {
    setLoadingDishes(true);
    fetch(`http://localhost:8080/api/v1/dishes/${id}`)
      .then((res) => res.json())
      .then((data) => {
        const normalized = data.map(dish => ({
          id: dish.IdDish,
          image: dish.image,
          name: dish.name,
          price: dish.price ? dish.price.toLocaleString('vi-VN') + "đ" : "",
          description: dish.description,
        }));
        setDishes(normalized);
        setLoadingDishes(false);
      })
      .catch(() => {
        setDishes([]);
        setLoadingDishes(false);
      });
  }, [id]);

  return (
    <>
      <Header />
      {/* Render thông tin nhà hàng */}
      {loadingRestaurant ? (
        <div style={{ textAlign: "center", margin: 32 }}>Đang tải thông tin nhà hàng...</div>
      ) : !restaurant ? (
        <div style={{ textAlign: "center", margin: 32, color: "red" }}>Không tìm thấy nhà hàng này.</div>
      ) : (
        <RestaurantDetailCard
          name={restaurant.name}
          address={restaurant.address}
          district={restaurant.district}
          average_rating={restaurant.average_rating}
          delivery_url={restaurant.delivery_url}
      
        />
      )}

      {/* Render danh sách món ăn */}
      {loadingDishes ? (
        <div style={{ textAlign: "center", margin: 32 }}>Đang tải danh sách món ăn...</div>
      ) : dishes.length === 0 ? (
        <div style={{ textAlign: "center", margin: 32 }}>Không có món ăn nào trong nhà hàng này.</div>
      ) : (
        <ListDishCard dishes={dishes} />
      )}

      <Footer />
    </>
  );
}
