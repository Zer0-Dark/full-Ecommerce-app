interface ScrollButtonsProps {
    onScrollLeft?: () => void;
    onScrollRight?: () => void;
}

function ScrollButtons({ onScrollLeft, onScrollRight }: ScrollButtonsProps) {
    return (
        <div className="text-3xl text-black absolute right-0 top-[15%] flex gap-5 ">
            <button onClick={onScrollLeft} className="w-12 h-12 rounded-full bg-secondryBg cursor-pointer hover:bg-secondryText">
                {"<"}
            </button>
            <button onClick={onScrollRight} className="w-12 h-12 rounded-full bg-secondryBg cursor-pointer hover:bg-secondryText">
                {">"}
            </button>

        </div>
    )
}

export default ScrollButtons;