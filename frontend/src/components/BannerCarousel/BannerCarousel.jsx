import React, { useState, useEffect } from "react";
import "./BannerCarousel.css";

const images = [
  "https://channel.mediacdn.vn/428462621602512896/2023/9/19/photo-1-1695121265877136843326.jpg",
  "https://marketingai.mediacdn.vn/603488451643117568/2024/6/3/image2-1717378852-503-width1920height1080-17174106165981891934676.png",
  "https://i.pinimg.com/originals/49/1e/e9/491ee929be5ce1c3eb05ff30ec6ed247.jpg",
];

function BannerCarousel() {
  const [current, setCurrent] = useState(0);
  const length = images.length;

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrent(prev => (prev + 1) % length);
    }, 3000); // 3 giây chuyển ảnh
    return () => clearInterval(interval);
  }, [length]);

  const nextSlide = () => setCurrent((current + 1) % length);
  const prevSlide = () => setCurrent((current - 1 + length) % length);

  return (
    <div className="banner-carousel">
      <button className="banner-arrow left" onClick={prevSlide}>&lt;</button>
      <img src={images[current]} alt={`Banner ${current}`} className="banner-image" />
      <button className="banner-arrow right" onClick={nextSlide}>&gt;</button>
      <div className="banner-dots">
        {images.map((_, idx) => (
          <span
            key={idx}
            className={`banner-dot ${idx === current ? "active" : ""}`}
            onClick={() => setCurrent(idx)}
          />
        ))}
      </div>
    </div>
  );
}

export default BannerCarousel;
