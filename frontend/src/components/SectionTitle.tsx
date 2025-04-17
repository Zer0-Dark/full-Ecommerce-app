

function SectionTitle({ sideTitle }: { sideTitle: string }) {
    return (
        <div className="text-secondryText font-bold text-xl flex gap-5 items-center">
            <div className="w-6 rounded-sm h-14 bg-secondryText">
            </div>
            <h2>{sideTitle}</h2>
        </div>
    )
}

export default SectionTitle;