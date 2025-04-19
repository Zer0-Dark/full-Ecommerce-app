import Image from "next/image"
import Link from "next/link"
import { useState, useEffect, useCallback } from "react"
import { AnimatePresence, motion } from "framer-motion"

// Banner data
const bannerImages = [
    { id: 1, src: "/banner-1.png", alt: "banner-1" },
    { id: 2, src: "/banner-2.png", alt: "banner-2" },
    { id: 3, src: "/banner-3.png", alt: "banner-3" },
]

function Banner({ style }: { style: string }) {
    const [currentIndex, setCurrentIndex] = useState(0)
    const [isAutoPlay, setIsAutoPlay] = useState(true)

    // Auto-slide function
    const nextSlide = useCallback(() => {
        setCurrentIndex((prev) => (prev === bannerImages.length - 1 ? 0 : prev + 1))
    }, [])

    // Auto-slide effect
    useEffect(() => {
        let interval: NodeJS.Timeout

        if (isAutoPlay) {
            interval = setInterval(() => {
                nextSlide()
            }, 5000) // Change slide every 5 seconds
        }

        return () => {
            if (interval) clearInterval(interval)
        }
    }, [isAutoPlay, nextSlide])

    // Pause auto-play on hover
    const handleMouseEnter = () => setIsAutoPlay(false)
    const handleMouseLeave = () => setIsAutoPlay(true)

    return (
        <div
            className={`${style} w-full relative overflow-hidden`}
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
        >
            <AnimatePresence mode="wait">
                <motion.div
                    key={currentIndex}
                    initial={{ opacity: 0.2, x: 100 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0.2, x: -100 }}
                    transition={{ duration: 0.2 }}
                >
                    <Link href="/">
                        <Image
                            className="w-full"
                            width={1500}
                            height={580}
                            alt={bannerImages[currentIndex].alt}
                            src={bannerImages[currentIndex].src}
                            priority
                        />
                    </Link>
                </motion.div>
            </AnimatePresence>

            {/* Navigation dots */}
            <div className="absolute bottom-[5%] left-1/2 transform -translate-x-1/2 flex flex-row gap-2">
                {bannerImages.map((_, index) => (
                    <button
                        key={index}
                        onClick={() => setCurrentIndex(index)}
                        className={`w-5 h-5 rounded-full transition duration-200 cursor-pointer
              ${currentIndex === index
                                ? 'bg-red-500 border-3 border-white'
                                : 'bg-white opacity-50 hover:opacity-75'}`}
                        aria-label={`Go to slide ${index + 1}`}
                    />
                ))}
            </div>


        </div>
    )
}

export default Banner;