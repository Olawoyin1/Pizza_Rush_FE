import React from 'react'
import Data from '../data'
import { Link } from 'react-router-dom'
import Headings from '../components/Headings'
import { TbCurrencyNaira } from "react-icons/tb";

const MenuPage = ({addProductToCart}) => {
  return (
    <div>
        <div className="container">

          <Headings heading={"Starters"} />

            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 ">
                {
                    Data.map(item=>(
                        <div key={item.id} className="item mb-4">
                        {/* =======PRODUCT IMAGE STARTS HERE======= */}
                        <div className="item-image rounded d-flex align-items-center justify-content-center">
                          <img src={item.image} loading="lazy" alt="" />
                          
                        </div>
  
                        {/* =======PRODUCT CONTENT STARTS HERE======= */}
                        <div className="item-details pt-2">
                          <Link
                            to={`/shop/${item.name}`}
                            className="fw-bolder nav-link"
                          >
                            {item.name}
                          </Link>
                          <div className="price d-flex align-items-center my-2 gap-3">
                            <small>
                              {item.description}
                            </small>
                          </div>
                            {/* <form action="" className="my-2">
                                  <select name="" id="">
                                  <option value="Medium">Medium</option>
                                  <option value="Large">Large</option>
                                  <option value="XLarge">XLarge</option>
                                  </select>
                              </form> */}
                              <button  onClick={() =>addProductToCart(item)}  className="button2 p-1 px-3 text-white">Add To cart <TbCurrencyNaira size={20} />  {item.price}</button>
                      
                        </div>
                      </div>
                    ))
                }
            </div>

            <Headings heading={"Classic Pizza"} />

            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 ">
                {
                    Data.map(item=>(
                        <div key={item.id} className="item mb-4">
                        {/* =======PRODUCT IMAGE STARTS HERE======= */}
                        <div className="item-image rounded d-flex align-items-center justify-content-center">
                          <img src={item.image} loading="lazy" alt="" />
                          
                        </div>
  
                        {/* =======PRODUCT CONTENT STARTS HERE======= */}
                        <div className="item-details pt-2">
                          <Link
                            to={`/shop/${item.name}`}
                            className="fw-bolder nav-link"
                          >
                            {item.name}
                          </Link>
                          <div className="price d-flex align-items-center my-2 gap-3">
                            <small>
                              {item.description}
                            </small>
                          </div>
                            {/* <form action="" className="my-2">
                                  <select name="" id="">
                                  <option value="Medium">Medium</option>
                                  <option value="Large">Large</option>
                                  <option value="XLarge">XLarge</option>
                                  </select>
                              </form> */}
                              <button onClick={() =>addProductToCart(item)} className="button2 p-1 px-3 text-white">Add To cart <TbCurrencyNaira size={20} /> {item.price}</button>
                      
                        </div>
                      </div>
                    ))
                }
            </div>
        </div>
    </div>
  )
}

export default MenuPage