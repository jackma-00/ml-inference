FROM public.ecr.aws/lambda/python:3.10

COPY ./setup.py .
 
RUN pip install --no-cache-dir --upgrade --target "${LAMBDA_TASK_ROOT}" .

COPY ./inference "${LAMBDA_TASK_ROOT}"/inference

CMD ["inference.lambda_function.lambda_handler"]

