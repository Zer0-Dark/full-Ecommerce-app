

function SectionTitle({ sideTitle, mainTitle }: { sideTitle: string, mainTitle: string }) {
    return (
        <div className="my-10">
            <div className="text-secondryText font-bold text-xl flex gap-5 items-center">
                <div className="w-6 rounded-sm h-14 bg-secondryText">
                </div>
                <h3>{sideTitle}</h3>
            </div>

            <h2 className=" font-secondry text-5xl font-medium  mt-8  ">{mainTitle}</h2>
        </div>
    )
}

export default SectionTitle;