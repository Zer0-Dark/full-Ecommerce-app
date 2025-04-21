import React from 'react'

function Button({ name }: { name: string }) {
    return (
        <button
            className=" px-16 py-4 transition capitalize  duration-300  rounded bg-[#DB4444] hover:bg-[#db4444ac] gap-2.5 text-neutral-50 font-medium  cursor-pointer "
        >
            {name}
        </button>

    )
}

export default Button