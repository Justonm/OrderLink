import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

const OrderForm = () => {
    const formik = useFormik({
        initialValues: {
            name: "",
            tableNumber: "",
            menuSelection: "",
            contact: "",
        },
        validationSchema: Yup.object({
            name: Yup.string().required("Name is required"),
            tableNumber: Yup.number().required("Table number is required"),
            menuSelection: Yup.string().required("Select a menu item"),
        }),
        onSubmit: (values) => {
            alert("Order placed!");
            console.log(values);
        },
    });

    return (
        <form onSubmit={formik.handleSubmit}>
            <label>Name</label>
            <input type="text" {...formik.getFieldProps("name")} />
            {formik.touched.name && formik.errors.name && <div>{formik.errors.name}</div>}

            <label>Table Number</label>
            <input type="number" {...formik.getFieldProps("tableNumber")} />
            {formik.touched.tableNumber && formik.errors.tableNumber && <div>{formik.errors.tableNumber}</div>}

            <label>Menu Selection</label>
            <input type="text" {...formik.getFieldProps("menuSelection")} />
            {formik.touched.menuSelection && formik.errors.menuSelection && <div>{formik.errors.menuSelection}</div>}

            <label>Contact (Optional)</label>
            <input type="text" {...formik.getFieldProps("contact")} />

            <button type="submit">Place Order</button>
        </form>
    );
};

export default OrderForm;
