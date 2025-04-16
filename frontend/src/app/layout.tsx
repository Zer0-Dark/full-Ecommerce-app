
import React from "react";
import { Poppins } from "next/font/google";
import "./globals.css";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";

const poppins = Poppins({
  variable: "--font-poppins-sans",
  weight: "400",
  subsets: ["latin"]
});

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};
export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (

    <html lang="en" suppressHydrationWarning>
      <body suppressHydrationWarning
        className={poppins.className}
      >
        <Nav />
        {children}
        <Footer />
      </body>
    </html >
  );
}
