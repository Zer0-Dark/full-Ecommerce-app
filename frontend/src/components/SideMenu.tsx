// import Link from "next/link"

import Link from "next/link"


function SideMenu() {
    return (
        <div className="flex items-start w-full h-full text-xl flex-col border-r-1 border-gray-600 py-12 gap-8">
            <Link href="/">
                Toys
            </Link>
            <Link href="/">
                Electronics
            </Link>
            <Link href="/">
                Home
            </Link>
            <Link href="/">
                Books
            </Link>
            <Link href="/">
                Clothing
            </Link>

        </div>
    )
}

export default SideMenu