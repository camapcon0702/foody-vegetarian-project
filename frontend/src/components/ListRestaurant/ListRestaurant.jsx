import React, { useState } from "react";
import './ListRestaurant.css';
import RestaurantCard from "../RestaurantCard/RestaurantCard";

const ITEMS_PER_PAGE = 8;

function getPageNumbers(current, total) {
  const delta = 2;
  const range = [];
  const rangeWithDots = [];
  let l;

  for (let i = 1; i <= total; i++) {
    if (
      i === 1 ||
      i === total ||
      (i >= current - delta && i <= current + delta)
    ) {
      range.push(i);
    }
  }

  for (let i of range) {
    if (l) {
      if (i - l === 2) {
        rangeWithDots.push(l + 1);
      } else if (i - l > 2) {
        rangeWithDots.push('...');
      }
    }
    rangeWithDots.push(i);
    l = i;
  }
  return rangeWithDots;
}

function ListRestaurant({ nameTitle, restaurants }) {
  const [currentPage, setCurrentPage] = useState(1);

  if (!restaurants || restaurants.length === 0) {
    return <div className="listrestaurant-empty">Không có nhà hàng nào để hiển thị.</div>;
  }

  const totalPages = Math.ceil(restaurants.length / ITEMS_PER_PAGE);
  const startIdx = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIdx = startIdx + ITEMS_PER_PAGE;
  const currentRestaurants = restaurants.slice(startIdx, endIdx);

  const goToPage = (page) => {
    if (typeof page !== "number" || page < 1 || page > totalPages) return;
    setCurrentPage(page);
  };

  return (
    <>
      <div className="title-list">{nameTitle}</div>
      <div className="listrestaurant-wrapper">
        {currentRestaurants.map((item) => (
          <RestaurantCard
            id={item.IdRestaurant}
            key={item.IdRestaurant + "_key"}
            name={item.name}
            address={item.address}
            district={item.district}
            average_rating={item.average_rating}
            delivery_url={item.delivery_url}
            image="data:image/png;base64,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"
          />
        ))}
      </div>
      {/* Smart Pagination */}
      <div className="pagination">
        <button onClick={() => goToPage(currentPage - 1)} disabled={currentPage === 1}>
          &lt; Trước
        </button>
        {getPageNumbers(currentPage, totalPages).map((page, idx) =>
          page === '...' ? (
            <span key={ + "_key_pagnigation"} className="pagination-ellipsis">...</span>
          ) : (
            <button
              key={page}
              className={currentPage === page ? "active" : ""}
              onClick={() => goToPage(page)}
            >
              {page}
            </button>
          )
        )}
        <button onClick={() => goToPage(currentPage + 1)} disabled={currentPage === totalPages}>
          Tiếp &gt;
        </button>
      </div>
    </>
  );
}

export default ListRestaurant;
