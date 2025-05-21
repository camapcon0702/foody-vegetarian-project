import React, { useEffect, useState } from 'react'
import Header from '../components/Header/Header'
import BannerCarousel from '../components/BannerCarousel/BannerCarousel'
import Footer from '../components/Footer/Footer'
import ListRestaurant from '../components/ListRestaurant/ListRestaurant'
import { getAllRestaurants } from '../api/restaurantApi'

export default function HomePage() {
    
  const [restaurants, setRestaurants] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getAllRestaurants()
      .then(data => {
        setRestaurants(data);
        setLoading(false);
      })
      .catch(err => {
        setError("Có lỗi khi lấy dữ liệu nhà hàng");
        setLoading(false);
      });
  }, []);

  return (
    <>
  
    
     
      <Header />
      <BannerCarousel/>
      {loading && <div style={{ textAlign: "center", margin: "30px" }}>Đang tải dữ liệu nhà hàng...</div>}
      {error && <div style={{ color: "red", textAlign: "center" }}>{error}</div>}
      {!loading && !error && <ListRestaurant nameTitle={"Danh sách các quán ăn"} restaurants={restaurants} />}
      <Footer />
    </>
  )
}
