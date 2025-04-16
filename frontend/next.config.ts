import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images:{
    remotePatterns:[new URL('https://www.w3.org/People/mimasa/test/imgformat/img/w3c_home.png')]
  }
};

export default nextConfig;
