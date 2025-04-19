'use client';
import Banner from '@/components/Banner';
import ProductCard from '@/components/ProductCard';
import SectionTitle from '@/components/SectionTitle';
import SideMenu from '@/components/SideMenu';
import axios from 'axios';
import { useState, useEffect } from 'react';
export default function Home() {


  const [products, setProducts] = useState([]);


  useEffect(() => {
    axios.get('https://zeyadashraf.pythonanywhere.com/products')
      .then(res => {
        setProducts(res.data.results);
      }).catch(error => {
        console.log("Error", error);
      })
  }, [])

  const renderedProducts = products.map((prod: { id: number, name: string, price: number, average_rating: string, reviews: [] }) => (<ProductCard key={prod.id} name={prod.name} price={prod.price} averageRating={prod.average_rating} reviews={prod.reviews.length} />));



  return (

    <div className='w-full mb-24 n px-[11%]' suppressHydrationWarning >
      {/* hero panel */}
      <div className='flex gap-10 w-full mb-18'>
        <div className='w-1/4'>
          <SideMenu />
        </div>
        <Banner style='pt-12' />
      </div>
      {/* end hero panel */}
      {/* flash sales? */}
      <SectionTitle mainTitle='Flash Sales' sideTitle={`Today's`} />
      <div className='flex flex-wrap gap-6 justify-between'>
        {renderedProducts}
        <div className="w-[270px] h-0 "></div>
        <div className="w-[270px] h-0 "></div>
        <div className="w-[270px] h-0 "></div>


      </div>


    </div>
  );
}
