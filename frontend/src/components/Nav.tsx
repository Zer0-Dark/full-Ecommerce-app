"use client";
import { useState } from "react";
import Link from "next/link"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons/faMagnifyingGlass";
import { faHeart } from "@fortawesome/free-solid-svg-icons";
import { faCartShopping } from "@fortawesome/free-solid-svg-icons";
function Nav() {
    const [language, setLanguage] = useState("English");

    const handleLanguageChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setLanguage(e.target.value);
    };

    return (
        <div>
            {/* upper menu */}
            <div className="bg-black text-white p-3 flex lg:flex-row flex-col flex-nowrap justify-center align-middle relative lg:text-base text-sm lg:pb-4 pb-10 ">
                <div className="flex ">
                    <h2 className="font-light">Summer Sale for All Swim Suits And Free Express Delivery - OFF 50%! </h2>
                    <a href="google.com" className="underline font-bold ml-4">Shop Now</a>
                </div>
                <div className="lg:absolute  lg:right-[8%] lg:top-1/2 lg:transfrom lg:-translate-y-1/2 flex items-center">
                    <div className="relative ">
                        <select
                            value={language}
                            onChange={handleLanguageChange}
                            className="bg-black text-white outline-none cursor-pointer appearance-none pl-3 pr-8 py-1  transition-colors duration-200"
                        >
                            <option value="English">English</option>
                            <option value="Arabic">Arabic</option>
                        </select>
                        <div className="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none">
                            <svg className="w-4 h-4 fill-current text-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" />
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
            {/* upper menu */}

            {/* The nav bar */}
            <div className=" flex flex-row flex-nowrap justify-around border-b-1 border-black pt-10 pb-6 items-center lg:px-20  ">
                <h2 className="text-3xl font-black">Exclusive</h2>
                <div className="lg:flex hidden space-x-8  ">
                    {[
                        { name: 'Home', path: '/' },
                        { name: 'Contact', path: '/contact' },
                        { name: 'About', path: '/about' },
                        { name: 'Sign Up', path: '/signup' }
                    ].map((item) => (
                        <Link
                            key={item.name}
                            className="border-b-2 border-transparent hover:border-current transition-all duration-300"
                            href={item.path}
                        >
                            {item.name}
                        </Link>
                    ))}
                </div>

                <div className="flex justify-between">
                    <div className="lg:flex hidden align-middle bg-secondryBg justify-items-center items-center relative">
                        <input className="px-6 py-2 w-58  text-sm bg-secondryBg outline-0" placeholder="What are you looking for?"></input>
                        <button onClick={() => console.log("clicked the search")} className="flex justify-center cursor-pointer items-center mr-4">
                            <FontAwesomeIcon className="text-black h-4 " icon={faMagnifyingGlass}></FontAwesomeIcon>
                        </button>
                    </div>
                    <div className="flex ml-4 space-x-4 justify-center items-center">
                        <FontAwesomeIcon className="h-4 cursor-pointer" icon={faHeart}></FontAwesomeIcon>
                        <FontAwesomeIcon className="h-4 cursor-pointer" icon={faCartShopping}></FontAwesomeIcon>
                    </div>
                </div>
            </div>
            {/* The nav bar */}


        </div>
    )
}

export default Nav