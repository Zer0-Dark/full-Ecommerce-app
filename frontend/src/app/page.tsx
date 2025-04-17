'use client';
import Banner from '@/components/Banner';
import SideMenu from '@/components/SideMenu';
// import axios from 'axios';
import { useState } from 'react';
export default function Home() {

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [products, setProducts] = useState();



  // useEffect(() => {
  //   axios.get('https://zeyadashraf.pythonanywhere.com/products')
  //     .then(res => {
  //       setProducts(res.data.results);
  //     }).catch(error => {
  //       console.log("Error", error);
  //     })
  // }, [])



  return (

    <div className='h-dvh w-full n px-[11%]' suppressHydrationWarning >
      <div className='flex gap-10 w-full'>
        <div className='w-1/4'>
          <SideMenu />
        </div>
        <Banner style='pt-12' />
      </div>

    </div>
  );
}
