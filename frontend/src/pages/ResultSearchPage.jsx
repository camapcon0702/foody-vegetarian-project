import React, { useEffect, useState } from 'react';
import { useLocation } from "react-router-dom";
import Header from '../components/Header/Header';
import Footer from '../components/Footer/Footer';
import ListRestaurant from '../components/ListRestaurant/ListRestaurant';
import './ResultSearchPage.css';

export default function ResultSearchPage() {
  const [restaurants, setRestaurants] = useState([]);
  const [loading, setLoading] = useState(false);

  // Lấy từ khóa từ query string
  const { search } = useLocation();
  const params = new URLSearchParams(search);
  const keyword = params.get("name");

  useEffect(() => {
    if (!keyword) {
      setRestaurants([]);
      return;
    }
    setLoading(true);
    fetch(`http://localhost:8080/api/v1/restaurants/search-by-dish?name=${encodeURIComponent(keyword)}`)
      .then(res => res.json())
      .then(data => {
        setRestaurants(data);
        setLoading(false);
      })
      .catch(() => {
        setRestaurants([]);
        setLoading(false);
      });
  }, [keyword]);

  return (
    <>
      <Header />
      <div className='response-data'></div>
      {loading ? (
        <div style={{ textAlign: "center", margin: 32 }}>Đang tìm kiếm...</div>
      ) : (
        <ListRestaurant nameTitle={`Kết quả tìm kiếm: "${keyword || ""}"`} restaurants={restaurants} />
      )}
      <Footer />
    </>
  );
}
