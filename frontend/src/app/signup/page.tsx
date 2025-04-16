'use client';
import Link from "next/link";
import React, { useState } from "react";

const SignUpForm: React.FC = () => {
    const [formData, setFormData] = useState({
        name: "",
        emailOrPhone: "",
        password: "",
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        console.log("Form submitted:", formData);
        // Here you would typically handle the form submission, like sending data to an API
    };

    return (
        <div className="flex items-center justify-between  flex-wrap  max-md:max-w-full lg:mb-0 mb-12 ">
            <div className="bg-[rgba(203,228,232,1)] self-stretch min-w-60 overflow-hidden  lg:w-1/2 w-full  pt-[75px]  max-md:max-w-full">
                <img
                    src="https://cdn.builder.io/api/v1/image/assets/TEMP/68ab25358f5a145bbedfd46720b32142553be900?placeholderIfAbsent=true"
                    className="aspect-[1.14] object-contain w-full max-md:max-w-full"
                    alt="Sign up illustration"
                />
            </div>
            <div className="self-stretch flex min-w-60 flex-col justify-center lg:w-1/2 w-full items-center py-10 ">
                <div className="text-black">
                    <h1 className="text-4xl font-medium leading-none tracking-[1.44px]">
                        Create an account
                    </h1>
                    <p className="text-base font-normal mt-6">Enter your details below</p>
                </div>
                <form
                    onSubmit={handleSubmit}
                    className="flex flex-col items-center mt-12 max-md:mt-10"
                >
                    <div className="max-w-full w-[370px]">
                        <div className="w-full">
                            <label htmlFor="name" className="sr-only">
                                Name
                            </label>
                            <input
                                type="text"
                                id="name"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                placeholder="Name"
                                className="text-black text-base font-normal focus:opacity-100 opacity-40 bg-transparent w-full outline-none"
                                onFocus={(e) => e.currentTarget.parentElement?.querySelector('.border-line')?.classList.replace('opacity-10', 'opacity-80')}
                                onBlur={(e) => e.currentTarget.parentElement?.querySelector('.border-line')?.classList.replace('opacity-80', 'opacity-10')}
                            />
                            <div className="w-full mt-2">
                                <div className="border border-line opacity-10 bg-black shrink-0 h-px border-black border-solid transition-opacity duration-300" />
                            </div>
                        </div>
                        <div className="w-full mt-10">
                            <label htmlFor="emailOrPhone" className="sr-only">
                                Email or Phone Number
                            </label>
                            <input
                                type="text"
                                id="emailOrPhone"
                                name="emailOrPhone"
                                value={formData.emailOrPhone}
                                onChange={handleChange}
                                placeholder="Email or Phone Number"
                                className="text-black text-base font-normal focus:opacity-100 opacity-40 bg-transparent w-full outline-none"
                                onFocus={(e) => e.currentTarget.parentElement?.querySelector('.border-line')?.classList.replace('opacity-10', 'opacity-80')}
                                onBlur={(e) => e.currentTarget.parentElement?.querySelector('.border-line')?.classList.replace('opacity-80', 'opacity-10')}
                            />
                            <div className="w-full mt-2">
                                <div className="border border-line opacity-10 bg-black shrink-0 h-px border-black border-solid transition-opacity duration-300" />
                            </div>
                        </div>
                        <div className="w-full mt-10">
                            <label htmlFor="password" className="sr-only">
                                Password
                            </label>
                            <input
                                type="password"
                                id="password"
                                name="password"
                                value={formData.password}
                                onChange={handleChange}
                                placeholder="Password"
                                className="text-black text-base font-normal focus:opacity-100 opacity-40 bg-transparent w-full outline-none"
                                onFocus={(e) => e.currentTarget.parentElement?.querySelector('.border-line')?.classList.replace('opacity-10', 'opacity-80')}
                                onBlur={(e) => e.currentTarget.parentElement?.querySelector('.border-line')?.classList.replace('opacity-80', 'opacity-10')}
                            />
                            <div className="w-full mt-2">
                                <div className="border border-line opacity-10 bg-black shrink-0 h-px border-black border-solid transition-opacity duration-300" />
                            </div>
                        </div>
                    </div>
                    <div className="text-base mt-10 w-[370px]">
                        <button
                            type="submit"
                            className="w-full transition duration-300 self-stretch rounded bg-[#DB4444] hover:bg-[#db4444ac] gap-2.5 text-neutral-50 font-medium px-[122px] py-4 max-md:px-5 cursor-pointer "
                        >
                            Create Account
                        </button>
                        <div className="flex flex-col items-center text-black mt-4">
                            <button
                                type="button"
                                className="w-full cursor-pointer rounded border flex flex-col items-stretch font-normal justify-center px-[80px] py-4 border-[rgba(0,0,0,0.4)] border-solid max-md:px-5 hover:bg-black hover:text-white transition duration-300"
                            >
                                <div className="flex gap-4 justify-center">
                                    <img
                                        src="https://cdn.builder.io/api/v1/image/assets/TEMP/ee061a163c52e61f1904b48b0ed48374916d6dc4?placeholderIfAbsent=true"
                                        className="aspect-[1] object-contain w-6 shrink-0"
                                        alt="Google icon"
                                    />
                                    <span>Sign up with Google</span>
                                </div>
                            </button>
                            <div className="flex items-center gap-4 mt-8">
                                <div className="font-normal opacity-70 self-stretch my-auto">
                                    Already have account?
                                </div>
                                <div className="self-stretch font-medium w-[47px] my-auto">
                                    <Link href="/" className="opacity-70">Log in</Link>
                                    <img
                                        src="https://cdn.builder.io/api/v1/image/assets/TEMP/f38bfafac761ba3e2fc5483f576d5862fa6ce250?placeholderIfAbsent=true"
                                        className="aspect-[47.62] object-contain w-[47px] mt-1"
                                        alt="Login underline"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default SignUpForm;
