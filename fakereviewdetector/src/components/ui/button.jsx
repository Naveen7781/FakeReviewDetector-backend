import React from "react";
import { cn } from "@/lib/utils";

const Button = ({ className, variant = "default", size = "default", asChild, ...props }) => {
  const Component = asChild ? "span" : "button";

  const baseStyles = "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50";
  
  const variantStyles = {
    default: "bg-blue-500 text-white hover:bg-blue-600",
    destructive: "bg-red-500 text-white hover:bg-red-600",
    outline: "border border-gray-300 bg-white hover:bg-gray-100",
    secondary: "bg-gray-500 text-white hover:bg-gray-600",
    ghost: "hover:bg-gray-100",
    link: "text-blue-500 underline hover:text-blue-700",
  };

  const sizeStyles = {
    default: "h-10 px-4 py-2",
    sm: "h-8 px-3 text-sm",
    lg: "h-12 px-6 text-lg",
    icon: "h-10 w-10 flex items-center justify-center",
  };

  return (
    <Component
      className={cn(baseStyles, variantStyles[variant], sizeStyles[size], className)}
      {...props}
    />
  );
};

export default Button;
