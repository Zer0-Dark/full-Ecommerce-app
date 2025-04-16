import React from 'react'
import Image from 'next/image'

function Product({ title, paragraph, img }: { title: string, paragraph: string, img: string }) {
    return (
        <div>
            <Image src={img} alt='testing'></Image>
            <h2>{title}</h2>
            <p>{paragraph}</p>
        </div>
    )
}

export default Product