import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Header.css";

function Header() {
  const [keyword, setKeyword] = useState("");
  const navigate = useNavigate();

  const handleInputChange = (e) => setKeyword(e.target.value);

  const handleSearch = (e) => {
    e.preventDefault();
    if (!keyword.trim()) return;
    navigate(`/search?name=${encodeURIComponent(keyword.trim())}`);
  };

  const handleLogoClick = () => {
    navigate("/");
  };

  return (
    <div className="container">
      <header className="header">
        <div className="header__left">
          <img
            src="https://www.foody.vn/style/images/logo/foody-vn.png"
            alt="Foody.vn"
            className="header__logo"
            style={{ cursor: "pointer" }}
            onClick={handleLogoClick}
          />
          <div className="header__city">
            Đà Nẵng <span className="header__dropdown">&#9660;</span>
          </div>
          <div className="header__category">
            Đồ Chay <span className="header__dropdown">&#9660;</span>
          </div>
          <form onSubmit={handleSearch} style={{ display: "flex" }}>
            <input
              type="text"
              className="header__search"
              placeholder="Địa điểm, món ăn, loại hình..."
              value={keyword}
              onChange={handleInputChange}
            />
            <button className="header__searchBtn" type="submit">
              <span className="header__icon">&#128269;</span>
            </button>
          </form>
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
