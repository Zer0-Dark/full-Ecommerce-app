import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'www.w3.org',
        pathname: '/People/mimasa/test/imgformat/img/**',
      },
    ],
  },

    allowedDevOrigins: ['192.168.56.1', '192.168.1.106', 'local-origin.dev', '*.local-origin.dev'],

};

export default nextConfig;
