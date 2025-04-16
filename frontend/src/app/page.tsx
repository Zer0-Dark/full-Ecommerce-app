'use client';
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

    <div className='h-dvh' suppressHydrationWarning >

      <h1 className="text-3xl font-bold  ">
        Testing the website
      </h1>

      <div>

      </div>

    </div>
  );
}
