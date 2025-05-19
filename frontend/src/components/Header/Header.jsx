import React from "react";
import "./Header.css";

function Header() {
  return (
    <div className="container">
      <header className="header">
      <div className="header__left">
        <img
          src="https://www.foody.vn/style/images/logo/foody-vn.png"
          alt="Foody.vn"
          className="header__logo"
        />
        <div className="header__city">
          Đà Nẵng <span className="header__dropdown">&#9660;</span>
        </div>
        <div className="header__category">
          Đồ Chay <span className="header__dropdown">&#9660;</span>
        </div>
        <input
          type="text"
          className="header__search"
          placeholder="Địa điểm, món ăn, loại hình..."
        />
        <button className="header__searchBtn">
          <span className="header__icon">&#128269;</span>
        </button>
      </div>
      <div className="header__right">
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSY2VgbS9-a39bD8_1n0fMeSlomQH1VR1LDUe1fvi7m5clQLkOAEbZwXCnEf3w&s=10"
          alt="VN Flag"
          className="header__flag"
        />
      </div>
    </header>
    </div>
    
  );
}

export default Header;
