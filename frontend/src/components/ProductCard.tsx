import Image from "next/image"
import Link from "next/link"

function ProductCard({ name, price, reviews, averageRating }: { name: string, price: number, reviews: number, averageRating: string }) {
    return (
        <Link className=" " href="/">
            <div className=" font-semibold w-[270px]">
                <div className="px-12 py-18 rounded-xl bg-secondryBg">

                    <Image src="/product-1.png" width={270} height={250} alt="product"></Image>
                </div>
                <div className="flex flex-col gap-2 mt-4">
                    <h2 className="">{name}</h2>
                    <div className="flex gap-3 ">
                        <p className=" text-secondryText">{price}</p>
                        {/* {
                            <p className=" opacity-50 line-through"> $160</p>
                        } */}
                    </div>

                    <div className="flex gap-5">
                        <div className="flex">
                            {[1, 2, 3, 4, 5].map((star) => {
                                const rating = +averageRating; // Replace with your actual rating
                                return (
                                    <span key={star} className="relative inline-block w-6 h-6">
                                        {/* Empty star (background) */}
                                        <svg
                                            className="w-full h-full text-gray-300"
                                            fill="currentColor"
                                            viewBox="0 0 20 20"
                                        >
                                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.8-2.034c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z" />
                                        </svg>

                                        {/* Filled star (overlay with width based on rating) */}
                                        <span
                                            className="absolute top-0 left-0 overflow-hidden"
                                            style={{
                                                width: `${rating >= star
                                                    ? '100%'
                                                    : rating > star - 1
                                                        ? `${(rating - (star - 1)) * 100}%`
                                                        : '0%'
                                                    }`
                                            }}
                                        >
                                            <svg
                                                className="w-6 h-6 text-yellow-400"
                                                fill="currentColor"
                                                viewBox="0 0 20 20"
                                            >
                                                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.8-2.034c-.783-.57-.38-1.81.588-1.81h3.462a1 1 0 00.95-.69l1.07-3.292z" />
                                            </svg>
                                        </span>
                                    </span>
                                );
                            })}
                        </div>
                        <p>({reviews})</p>
                    </div>
                </div>
            </div>
        </Link>
    )
}

export default ProductCard