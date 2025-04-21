'use client';
import Banner from '@/components/Banner';
import ScrollButtons from '@/Ui/ScrollButtons';
import ProductCard from '@/components/ProductCard';
import SectionTitle from '@/components/SectionTitle';
import SideMenu from '@/components/SideMenu';
import axios from 'axios';
import { useState, useEffect, useRef } from 'react';
import Button from '@/Ui/Button';
import Hr from '@/Ui/Hr';
import Category from '@/components/Category';
export default function Home() {

  const [gapBetweenProducts, setGapBetweenProducts] = useState(0);
  const [products, setProducts] = useState([]);
  const productsContainerRef = useRef<HTMLDivElement>(null); // Add ref

  useEffect(() => {
    axios.get('https://zeyadashraf.pythonanywhere.com/products')
      .then(res => {
        setProducts(res.data.results);
      }).catch(error => {
        console.log("Error", error);
      })
  }, [])

  const renderedProducts = products.map((prod: { id: number, name: string, price: number, average_rating: string, reviews: [] }) => (<ProductCard key={prod.id} name={prod.name} price={prod.price} averageRating={prod.average_rating} reviews={prod.reviews.length} />));

  useEffect(() => {
    const marginOfScreen = window.innerWidth * (22 / 100);
    const productsCount = Math.floor((window.innerWidth - marginOfScreen) / 270);
    const remainingSpace = (window.innerWidth - marginOfScreen) % 270;

    // Calculate gap size with minimum of 9px
    const calculatedGap = remainingSpace / (productsCount - 1 || 1);
    const finalGap = Math.max(calculatedGap, 9); // Ensure minimum 9px gap

    setGapBetweenProducts(finalGap);
  }, [])
  // The scroll functionality of the button 
  // Scroll functions
  const scrollLeft = () => {
    if (productsContainerRef.current) {
      const marginOfScreen = window.innerWidth * (22 / 100);
      const theProductsGaps = Math.max(gapBetweenProducts, 9); // Ensure minimum 9px
      const scrollItems = Math.floor((window.innerWidth - marginOfScreen) / (270 + theProductsGaps));
      const screenWidth = scrollItems * (270 + theProductsGaps);
      productsContainerRef.current.scrollBy({ left: -screenWidth, behavior: 'smooth' });
    }
  };

  const scrollRight = () => {
    if (productsContainerRef.current) {
      const marginOfScreen = window.innerWidth * (22 / 100);
      const theProductsGaps = Math.max(gapBetweenProducts, 9); // Ensure minimum 9px
      const scrollItems = Math.floor((window.innerWidth - marginOfScreen) / (270 + theProductsGaps));
      const screenWidth = scrollItems * (270 + theProductsGaps);
      productsContainerRef.current.scrollBy({ left: screenWidth, behavior: 'smooth' });
    }
  };

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
      <div className='relative mb-12 '>
        <SectionTitle mainTitle='Flash Sales' sideTitle={`Today's`} />
        <ScrollButtons onScrollLeft={scrollLeft} onScrollRight={scrollRight} />
        <div
          ref={productsContainerRef}
          className="flex flex-nowrap overflow-x-auto overflow-y-hidden justify-between"
          style={{
            gap: `${Math.max(gapBetweenProducts, 9)}px`,
            scrollbarWidth: 'none',
            msOverflowStyle: 'none'
          }}
        >
          {renderedProducts}
          <div className="w-[270px] h-0"></div>
          <div className="w-[270px] h-0"></div>
          <div className="w-[270px] h-0"></div>
        </div>
        <div className='w-full flex justify-center mt-12 items-center'>
          <Button name='view all products' />
        </div>
      </div >
      {/* end flash sales */}
      <Hr />
      {/* start categories area */}
      <div className=''>
        <div className=' relative'>
          <SectionTitle sideTitle='Categories' mainTitle='Browse By Category' />
          <ScrollButtons />
          <div className='flex gap-4 flex-nowrap overflow-hidden w-full'>
            <Category type='Phones' />
            <Category type='Computers' />
            <Category type='Smart Watches' />
            <Category type='Camera' />
            <Category type='Headphones' />
            <Category type='Gaming' />


          </div>
        </div>
      </div>
    </div>
  );
}
