

function SectionTitle({ sideTitle, mainTitle }: { sideTitle: string, mainTitle: string }) {
    return (
        <div className="my-10">
            <div className="text-secondryText font-bold flex gap-4 items-center">
                <div className="w-6 rounded-sm h-12 bg-secondryText">
                </div>
                <h3 className="font-semibold">{sideTitle}</h3>
            </div>

            <h2 className=" font-secondry text-4xl font-medium  mt-8  ">{mainTitle}</h2>
        </div>
    )
}

export default SectionTitle;