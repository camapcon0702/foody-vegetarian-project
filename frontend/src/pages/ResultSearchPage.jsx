import React from 'react'

import Header from '../components/Header/Header'
import Footer from '../components/Footer/Footer'
import ListRestaurant from '../components/ListRestaurant/ListRestaurant' 
import './ResultSearchPage.css'

 const fakeRestaurants = [
    {
      IdRestaurant: 1,
      name: "Quán Chay Ngon",
      address: "100 Lê Lợi, Q. Hải Châu",
      district: "Hải Châu",
      average_rating: 8.2,
      delivery_url: "https://shopeefood.vn/da-nang/quan-chay-ngon",
      image: "https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45",
    },
    {
      IdRestaurant: 2,
      name: "Nhà Hàng Vegan Đà Nẵng",
      address: "45 Nguyễn Văn Linh, Q. Thanh Khê",
      district: "Thanh Khê",
      average_rating: 7.8,
      delivery_url: "https://shopeefood.vn/da-nang/vegan-da-nang",
      image: "https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45",
    },
    {
      IdRestaurant: 3,
      name: "Chay Tịnh Tâm",
      address: "22 Phan Châu Trinh, Q. Hải Châu",
      district: "Hải Châu",
      average_rating: 8.0,
      delivery_url: "https://shopeefood.vn/da-nang/chay-tinh-tam",
      image: "https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45",
    },
    {
      IdRestaurant: 4,
      name: "Quán Chay Bồ Đề",
      address: "12 Núi Thành, Q. Cẩm Lệ",
      district: "Cẩm Lệ",
      average_rating: 7.3,
      delivery_url: "https://shopeefood.vn/da-nang/quan-chay-bo-de",
      image: "https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45",
    },
    {
      IdRestaurant: 5,
      name: "Quán Chay Nga",
      address: "296 Đống Đa, P. Thanh Bình",
      district: "Hải Châu",
      average_rating: 7.4,
      delivery_url: "https://shopeefood.vn/da-nang/quan-chay-nga",
      image: "https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45",
    },
    {
      IdRestaurant: 6,
      name: "Nhà Hàng Chay Tâm Ý",
      address: "80 Phạm Văn Nghị, Q. Thanh Khê",
      district: "Thanh Khê",
      average_rating: 8.5,
      delivery_url: "https://shopeefood.vn/da-nang/chay-tam-y",
      image: "https://down-sp-sg.img.susercontent.com/vn-11134526-7r98o-lvoj2xv591mh45",
    }
  ];

export default function ResultSearchPage() {
  return (
    <>
        <Header/>
        <div className='response-data'></div>
            <ListRestaurant nameTitle={"Kết quả tìm kiếm"} restaurants={fakeRestaurants}/>
        


      
    </>
  )
}
