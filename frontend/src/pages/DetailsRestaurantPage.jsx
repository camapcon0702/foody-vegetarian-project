import React from 'react'
import Header from '../components/Header/Header'
import RestaurantDetailCard from '../components/DetailsRestaurant/RestaurantDetailCard'
import ListDishCard from '../components/ListDishCard/ListDishCard'
import Footer from '../components/Footer/Footer'

export default function DetailsRestaurantPage() {
 
  const dishes = [
    {
      id: 1,
      image: "https://mms.img.susercontent.com/vn-11134517-7r98o-lz4mz2nqe3wtcb@resize_ss120x120!@crop_w120_h120_cT",
      name: "Combo Sáng Highlands (cỡ Nhỏ)",
      price: "39.000đ"
    },
    {
      id: 2,
      image: "https://mms.img.susercontent.com/vn-11134517-7r98o-lz4t9kp7xuapf4@resize_ss120x120!@crop_w120_h120_cT",
      name: "Bạc Xỉu Đá (S)",
      price: "29.000đ"
    },
    {
      id: 3,
      image: "https://mms.img.susercontent.com/vn-11134517-7r98o-lz4t9kp7xuapf4@resize_ss120x120!@crop_w120_h120_cT",
      name: "Trà sữa trân châu",
      price: "32.000đ"
    },
    {
      id: 4,
      image: "https://mms.img.susercontent.com/vn-11134517-7r98o-lz4t9kp7xuapf4@resize_ss120x120!@crop_w120_h120_cT",
      name: "Latte Đá",
      price: "35.000đ"
    },
    {
      id: 5,
      image: "https://mms.img.susercontent.com/vn-11134517-7r98o-lz4t9kp7xuapf4@resize_ss120x120!@crop_w120_h120_cT",
      name: "Caramel Macchiato Đá",
      price: "45.000đ"
    },
    {
      id: 6,
      image: "https://mms.img.susercontent.com/vn-11134517-7r98o-lz4vlezd1t41d4@resize_ss120x120!@crop_w120_h120_cT",
      name: "Bánh mì Việt (15-19cm)",
      price: "18.000đ"
    }
  ];

  return (
    <>
      <Header />
      <RestaurantDetailCard
        name="Quán ăn đẳng cấp"
        address="K36, Hoàng Diệu"
        district="Hải Châu"
        average_rating="7.6"
        delivery_url="#"
      />
      <ListDishCard dishes={dishes} />
      <Footer/>
    </>
  );
}
