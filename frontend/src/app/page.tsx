'use client';
import Banner from '@/components/Banner';
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
      <div className='flex justify-betwee w-full'>
        <div className='w-1/4'>

        </div>
        <Banner style='pt-12' />
      </div>

    </div>
  );
}
