import Image from 'next/image';

// Import category SVGs
const CategoryCamera = '/Category-Camera.svg';
const CategoryCellPhone = '/Category-CellPhone.svg';
const CategoryComputer = '/Category-Computer.svg';
const CategoryGamepad = '/Category-Gamepad.svg';
const CategoryHeadphone = '/Category-Headphone.svg';
const CategorySmartWatch = '/Category-SmartWatch.svg';

function Category({ type }: { type: string }) {
    const categories = [
        { name: 'Cameras', icon: CategoryCamera },
        { name: 'Phones', icon: CategoryCellPhone },
        { name: 'Computers', icon: CategoryComputer },
        { name: 'Gaming', icon: CategoryGamepad },
        { name: 'Headphones', icon: CategoryHeadphone },
        { name: 'Smart Watches', icon: CategorySmartWatch }
    ];

    const rendredType = categories.find(category => category.name === type) || categories[0];

    return (
        <div className='w-42 min-w-42 flex flex-col gap-1  py-8 justify-center items-center border-2 border-[#a6a6a6] rounded-md cursor-pointer hover:bg-secondryText hover:text-white transition duration-300 group ' >
            <Image className='group-hover:invert' src={rendredType.icon} width={56} height={56} alt='img'></Image>
            <h2>{rendredType.name}</h2>
        </div>
    )
}

export default Category