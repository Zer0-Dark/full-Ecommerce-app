import Image from "next/image"
import Link from "next/link"
import { faPaperPlane } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"

function Footer() {
    return (
        <footer className="w-full text-white bg-black ">
            <div className="flex relative items-start justify-between [&_h2]:text-xl [&_h2]:mb-6 py-18 px-30 [&_h2]:font-bold [&_div]:w-48 [&_div]:space-y-5 [&_p]:text-sm ">
                <div className="">
                    <h3 className="text-2xl mb-6 font-bold">Exclusive</h3>
                    <h4 className="text-xl mb-6">Subscribe</h4>
                    <p>Get 10% off your first order</p>
                    <div className="relative">
                        <FontAwesomeIcon className=" max-w-4  absolute right-2 top-1/2 -translate-y-1/2 cursor-pointer " icon={faPaperPlane}></FontAwesomeIcon>
                        <input className="p-2 pr-8 w-full  text-sm" placeholder="Enter Your email" type="text"></input>
                    </div>
                </div>
                <div>
                    <h2>Supoort</h2>
                    <p>111 Bijoy sarani, dhaka, dh 1515, Oman.</p>
                    <p>exclusive@gmail.com</p>
                    <p>+88015-8888-999</p>
                </div>
                <div className="flex flex-col">
                    <h2>Account</h2>
                    <Link href="/">
                        My Account
                    </Link>
                    <Link href="/">
                        Login / Register
                    </Link>
                    <Link href="/">
                        Cart
                    </Link>
                    <Link href="/">
                        Wishlist
                    </Link>
                    <Link href="/">
                        Shop
                    </Link>
                </div>
                <div>
                    <h2>Quick Link</h2>
                    <p>Privacy Policy</p>
                    <p>Terms Of Use</p>
                    <p>FAQ</p>
                    <p>Contact</p>
                </div>
                <div>
                    <h2>Download App</h2>
                    <p className=" opacity-70 !text-xs">Save $3 with App New User Only</p>
                    <div className="flex justify-between w-full ">
                        <Image className="w-1/2 mb-0" width="70" height="70" alt="Qr-code" src="/qr-code.png" />
                        <div className="flex flex-col justify-between   ml-4 w-1/2 h-[80px] ">
                            <Image className="mb-0 w-full cursor-pointer" width="40" height="0" alt="download-button" src="/google-play.png" />
                            <Image className="mb-0 w-full cursor-pointer" width="40" height="0" alt="download-button" src="/app-store.png" />
                        </div>
                    </div>
                    <div className="flex items-center gap-6 w-full">
                        <Image className="m-0 cursor-pointer" width={25} height={25} alt="social icon" src="/facebook.png"></Image>
                        <Image className="m-0 cursor-pointer" width={25} height={25} alt="social icon" src="/twitter.png"></Image>
                        <Image className="m-0 cursor-pointer" width={25} height={25} alt="social icon" src="/insta.png"></Image>
                        <Image className="m-0 cursor-pointer" width={25} height={25} alt="social icon" src="/linkedin.png"></Image>
                    </div>
                </div>
            </div>

            <div className="p-5 text-center border-t-1 border-white opacity-60">
                <p>@ Copyright Rimel 2022. All right reversed</p>
            </div>
        </footer>
    )
}

export default Footer